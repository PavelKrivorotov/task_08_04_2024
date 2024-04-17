import { defineStore } from "pinia";
import { ref, reactive } from 'vue';

import { fetchDocument, fetchDocuments } from "@/http/requests";

export const useDocumentStore = defineStore('documents', () => {
    const countDocumentsPerPage = ref(50)

    const currentPage = ref(1);
    const currentDocument = reactive({
        id: null,
        title: null,
        published: null,
        countWords: null,
    });
    const documents = reactive([]);

    async function loadDocument(id) {
        try {
            const result = await fetchDocument(id)
            const data = await result.json()
            setCurrentDocument(
                data['id'],
                data['title'],
                data['published'],
                data['count_words']
            )

        } catch (error) {
            return;
        }
    }

    async function loadDocuments() {
        try {
            const result = await fetchDocuments(currentPage.value)
            const data = await result.json()
    
            if (result.status == 200) {
                setDocuments(data['result'])
                currentPage.value += 1

            }

        } catch (error) {
            return;
        }
    }

    function setCurrentDocument(id, title, published, countWords) {
        currentDocument.id = id
        currentDocument.title = title
        currentDocument.published = published
        currentDocument.countWords = countWords
    }

    function setDocuments(data) {
        data.forEach(element => {
            documents.push({
                id: element['id'],
                title: element['title'],
                published: element['published'],
                countWords: element['count_words'],
            })
        })
    }

    function setDefault(currentDoc=true) {
        currentPage.value = 1

        if (currentDoc == true) {
            currentDocument.id = null
            currentDocument.title = null
            currentDocument.published = null
            currentDocument.countWords = null
        }

        documents.splice(0, documents.length)
    }

    return {
        countDocumentsPerPage,
        currentPage,
        currentDocument,
        documents,

        loadDocument,
        loadDocuments,

        setCurrentDocument,
        setDefault,
    }
});
