import React from 'react'

// utils
import { apiDownload } from '../../services/api'

// styles and images
import './FileBlock.scss'
import fileIcon from '../../assets/file.svg'
import trashIcon from '../../assets/trash.svg'
import { getDateFormatJSON, getFileNameFromURL } from '../../utils'


function FileBlock({ file, deleteFile }) {

    function handleDeleteFile(file) {
        // console.log('File Deleted!!')
        deleteFile(file)
    }

    async function downloadFile(event) {
        event.preventDefault()
        const token = localStorage.getItem('token')
        const {blob, response_status } = await apiDownload(`mybox/files/${ file.id }/download/`, token)
        if (response_status >= 400) {
            alert('Erro ao fazer download do arquivo')
            return
        }
        const newBlob = new Blob([blob])
        const blobUrl = window.URL.createObjectURL(newBlob)
        const link = document.createElement('a')
        link.href = blobUrl
        link.setAttribute(
            'download',
            `${ getFileNameFromURL(file.file, file.extension) }`
        )
        document.body.appendChild(link)
        link.click()
        link.parentNode.removeChild(link)
        window.URL.revokeObjectURL(blobUrl);
    }

    return (
        <li className="file-block">
            <a
                // href={ file.file }
                href={`mybox/files/${ file.id }/download/`}
                onClick={ event => downloadFile(event) }
            >
                <img src={ fileIcon } alt="File icon" />

                <strong>{ getFileNameFromURL(file.file, file.extension) }</strong>
            </a>

            <span>{ getDateFormatJSON(file.created_at) }</span>

            <img
                className="trash"
                src={ trashIcon }
                alt="Trash icon"
                onClick={ e => handleDeleteFile(file) }
            />
        </li>
    )
}

export default FileBlock