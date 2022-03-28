function title(pageTitle) {
    const mainTitle = 'Mybox'
    document.title = `${ pageTitle } | ${ mainTitle }`
}

function getDateFormatJSON(date){
    const dateArray = date.split('-').map(d => d.trim())
    return `${ dateArray[2] }/${ dateArray[1] }/${ dateArray[0] }`
}

function getFileNameFromURL(fileUrl){
    const urlSplit = fileUrl.split('/')
    return urlSplit[urlSplit.length - 1]
}

export { title, getDateFormatJSON, getFileNameFromURL }