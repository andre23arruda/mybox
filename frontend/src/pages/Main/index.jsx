import React, {useEffect, useState} from 'react'
import { Link, useHistory } from 'react-router-dom'
import axios from 'axios'

// components
import Header from '../../components/Header'
import Footer from '../../components/Footer'
import LogoutButton from '../../components/LogoutButton'
import FileBlock from '../../components/FileBlock'
import DropZone from 'react-dropzone'
import Progress from 'react-progressbar'

// utils
import { getApi, deleteApi } from '../../services/api'
import { title } from '../../utils'

// styles and images
import filePlusIcon from '../../assets/file-plus.svg'
import './Main.scss'


function Main() {
    title('My files')
    const history = useHistory()
    const [files, setFiles] = useState([])
    const [completed, setCompleted] = useState(0)
    const [authToken, setToken] = useState('')

    async function loadFilesList() {
        const token = localStorage.getItem('token')
        if (!token){
            history.push('/login')
            return
        }
        const { data, response_status } = await getApi(`mybox/files/`, token)
        if (response_status >= 400) {
            history.push('/login')
            return
        }
        console.log(data)
        setFiles(data)
        setToken(token)
    }

    useEffect(() => {
        loadFilesList()
    }, [history])

    function handleUpload(files) {
        console.log(files)
        const data = new FormData()
        files.forEach(file => {
            data.append('files', file)
        })
        for (var value of data.values()) {
            console.log(value)
        }

        axios.request({
            method: 'post',
            url:  `${ process.env.REACT_APP_API_URL }mybox/files/upload/`,
            data: data,
            headers: { 'Authorization': authToken },
            onUploadProgress: (p) => {
                console.log(p.loaded / p.total)
                setCompleted(100 * p.loaded / p.total)
            }
        }).then (data => {
            console.log('deu bom')
            alert(`Upload dos arquivos realizados com sucesso`)
            setCompleted(0)
            loadFilesList()
        })
    }

    async function deleFile(file) {
        const { response_status } = await deleteApi(`mybox/files/${ file.id }/`, authToken)
        if (response_status >= 400) {
            history.push('/login')
            return
        }
        setFiles(files.filter(obj => obj.id !== file.id))
    }

    function uploading() {
        return completed > 0
    }

    return (
        <>
        <Header title={ 'Meus arquivos' } />

        <div className="main-container">
            <DropZone onDropAccepted={ handleUpload } disabled={ uploading() }>
                {({ getRootProps, getInputProps }) => (
                    <div
                        className={ uploading() ? 'upload disabled' : 'upload' }
                        {...getRootProps()}
                    >
                        <input {...getInputProps()} />

                        <img src={ filePlusIcon } alt="File Plus icon" />

                        { uploading() ?  (
                            <p>Aguarde o upload dos arquivos</p>
                        ) : (
                            <p>Arraste arquivos ou clique aqui</p>
                        )
                        }

                    </div>
                )}
            </DropZone>

            <Progress completed={ completed } />

            <ul>
                { files.map(file => (
                    <FileBlock
                        file={ file }
                        deleFile={ deleFile }
                        key={ file.id }
                    />
                ))}
            </ul>

            <LogoutButton />

        </div>
            <Footer />
        </>
    )
}

export default Main
