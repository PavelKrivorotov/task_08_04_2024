<script setup>
import { ref } from 'vue';

import { useDocumentStore } from '@/pinia/document-store';
import { useDocumentWordStore } from '@/pinia/document-word-store';
import { uploadDocument } from '@/http/requests'

const docStore = useDocumentStore()
const wordStore = useDocumentWordStore()

const file = ref(null)

async function uploadFile() {
    if (file.value == null) {
        return;
    }
    
    const body = new FormData()
    body.append('file', file.value)

    try {
        const result = await uploadDocument(body)
        const data = await result.json()

        if (result.status == 201) {
            docStore.setDefault()
            await docStore.loadDocument(data['id'])
            await docStore.loadDocuments()
            await wordStore.initialLoadWords(data['id'])

            file.value = null
        }

    } catch (error) {
        return;
    }
}
</script>

<template>
    <v-card>
        <v-card-title>
            Upload new document
        </v-card-title>

        <v-card-text>
            <v-form>
                <v-file-input
                accept="text/plain"
                label="Input text document"
                v-model="file"
                ></v-file-input>
            </v-form>
        </v-card-text>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
            type="submit"
            color="secondary"
            @click="uploadFile"
            >
                submit
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<style scoped></style>
