function title(pageTitle) {
    const mainTitle = 'Mybox'
    document.title = `${ pageTitle } | ${ mainTitle }`
}

function getDateFormatJSON(date) {
    const dateArray = date.split('-').map(d => d.trim())
    return `${ dateArray[2] }/${ dateArray[1] }/${ dateArray[0] }`
}

function getFileNameFromURL(fileUrl, fileExtension) {
    const urlSplit = fileUrl.split('/')
    const fileName = urlSplit[urlSplit.length - 1]
    return fileName.endsWith(fileExtension) ? fileName : fileName + fileExtension
}

export { title, getDateFormatJSON, getFileNameFromURL }