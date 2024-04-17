import { defineStore } from "pinia";
import { ref, reactive } from 'vue';

import { fetchWords } from "@/http/requests";

export const useDocumentWordStore = defineStore('documnet-word', () => {
    const documentId = ref(null);

    const countWords = ref(0);
    const countWordsPerPage = ref(50);
    const words = reactive([]);
    const loading = ref(false)

    async function initialLoadWords(id) {
        await load(id, 1, true)
        documentId.value = id
    }

    async function loadWords({ page }) {
        if (documentId.value != null ) {
            await load(documentId.value, page)
        }
    }

    async function load(id, page, initial=false) {
        loading.value = true

        try {
            const result = await fetchWords(id, page)
            const data = await result.json()
    
            if (initial == true){
                documentId.value = id
                countWordsPerPage.value = data['count_per_page']
                countWords.value = data['count']
            }
        
            words.splice(0, words.length)
            setWords(data['result'])
    
            loading.value = false

        } catch (error) {
            return;
        }
    }

    function setWords(data) {
        data.forEach(element => {
            words.push({
                word: element['word'],
                tf: element['tf'],
                idf: element['idf']
            })
        })
    }

    function setDefault() {
        documentId.value = null

        countWords.value = 0
        countWordsPerPage.value = 50
        words.splice(0, words.length)
        loading.value = false
    }

    return {
        documentId,
        countWords,
        countWordsPerPage,
        words,
        loading,

        initialLoadWords,
        loadWords,

        setDefault
    }
});
