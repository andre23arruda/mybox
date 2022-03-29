import React, { useState } from 'react'

// utils
import { deleteApi } from '../../services/api'

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

    return (
        <li className="file-block">
            <a
                href={ file.file }
                target="_blank"
                rel="noopener noreferrer"
            >
                <img src={ fileIcon } alt="File icon" />

                <strong>{ getFileNameFromURL(file.file) }</strong>
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