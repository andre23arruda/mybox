import React, {useEffect, useState} from 'react'
import { Link, useHistory } from 'react-router-dom'


// components
import Header from '../../components/Header'
import Footer from '../../components/Footer'
import LogoutButton from '../../components/LogoutButton'
import FileBlock from '../../components/FileBlock'
import DropZone from 'react-dropzone'
import Progress from 'react-progressbar'

// utils
import { getApi, postFormDataApi } from '../../services/api'
import { title } from '../../utils'

// styles and images
import filePlusIcon from '../../assets/file-plus.svg'
import './Main.scss'


function Main() {
    title('My files')
    const history = useHistory()
    const [files, setFiles] = useState([
        { id: 1, name: 'File 1.png', created_at: '11/03/2022'},
        { id: 2, name: 'File 2.png', created_at: '11/03/2022'},
        { id: 3, name: 'File 3.png', created_at: '11/03/2022'},
        { id: 4, name: 'File 4.png', created_at: '11/03/2022'},
    ])

    // useEffect(() => {
    //     async function loadFilesList() {
    //         const token = localStorage.getItem('token')
    //         if (!token){
    //             history.push('/login')
    //             return
    //         }
    //         const routePrefix = token.startsWith('JWT') ? '' : 'oauth-'
    //         const { data, response_status } = await getApi(`mybox/${ routePrefix }files/`, token)
    //         if (response_status >= 400) {
    //             history.push('/login')
    //             return
    //         }
    //         setFiles(data)
    //     }
    //     loadFilesList()
    // }, [history])

    function handleUpload(files) {
        console.log(files)
        files.forEach(file => {
            const data = new FormData()
            data.append('files', file)
            // postFormDataApi(`rocketbox/files/upload/`, data)
        })
    }

    function deleFile(file) {
        setFiles(files.filter(obj => obj.id !== file.id))
    }

    return (
        <>
        <Header title={ 'Meus arquivos' } />

        <div className="main-container">
            <DropZone onDropAccepted={ handleUpload }>
                {({ getRootProps, getInputProps }) => (
                    <div className="upload" {...getRootProps()}>
                        <input {...getInputProps()} />

                        <img src={ filePlusIcon } alt="File Plus icon" />

                        <p>Arraste arquivos ou clique aqui</p>
                    </div>
                )}
            </DropZone>

            <Progress completed={ 75 } />

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
