import * as urls from './urls';


export async function uploadDocument(body) {
    try {
        const result = await fetch(
            urls.URL_DOCUMENTS_UPLOAD,
            {
                method: 'POST',
                body: body,
            }
        )
        return result
        
    } catch (error) {
        console.error('Error in `uploadDocument`: ', error)
    }
}

export async function fetchDocument(id) {
    try {
        const result = await fetch(urls.URL_DOCUMENTS_RETRIEVE.replace('$id', id))
        return result

    } catch (error) {
        console.error('Error in `fetchDocument`: ', error)
    }
}

export async function fetchDocuments(page) {
    try {
        const result = await fetch(urls.URL_DOCUMENTS_LIST.replace('$page', page))
        return result

    } catch (error) {
        console.error('Error in `fetchDocuments`: ', error)
    }
}

export async function removeDocument(id) {
    try {
        const result = await fetch(
            urls.URL_DOCUMENTS_DELETE.replace('$id', id),
            {
                method: 'DELETE'
            }
        )
        return result
        
    } catch (error) {
        console.log('Error in `removeDocument`: ', error)
    }
}

export async function fetchWords(id, page) {
    var url = urls.URL_DOCUMENTS_WORDS_LIST.replace('$id', id)
    url = url.replace('$page', page)

    try {
        const result = await fetch(url)
        return result

    } catch (error) {
        console.error('Error in `fetchWords`: ', error)
    }
}

