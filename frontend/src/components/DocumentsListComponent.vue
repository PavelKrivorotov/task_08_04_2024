<script setup>
import { reactive, onMounted } from 'vue';

import { useDocumentStore } from '@/pinia/document-store';
import { useDocumentWordStore } from '@/pinia/document-word-store';

import { removeDocument } from '@/http/requests';

const docStore = useDocumentStore()
const wordStore = useDocumentWordStore()

const confirmDialog = reactive({
    isActive: false,
    item: null
})

async function selectItem(item) {
    docStore.setCurrentDocument(
        item.id,
        item.title,
        item.published,
        item.countWords
    )

    await wordStore.initialLoadWords(item.id)
}

async function deleteItem(item) {
    try {
        const result = await removeDocument(item.id)

        if (result.status == 204) {
            if (item.id == docStore.currentDocument.id) {
                docStore.setDefault()
                wordStore.setDefault()

            } else {
                docStore.setDefault(false)
                wordStore.setDefault()
                await wordStore.initialLoadWords(docStore.currentDocument.id)
            }

            await docStore.loadDocuments()
        }

    } catch (error) {
        return;
    }
}

function openDialog(item) {
    confirmDialog.isActive = true
    confirmDialog.item = item
}

async function acceptDialog() {
    confirmDialog.isActive = false
    await deleteItem(confirmDialog.item)
}

async function refuseDialog() {
    confirmDialog.isActive = false
}

onMounted(async () => {
    docStore.loadDocuments()
})
</script>

<template>
    <v-card
    class="mx-auto"
    max-width="500"
    >
        <v-card-title>
            Uploaded documents
        </v-card-title>

        <v-divider></v-divider>

        <v-virtual-scroll
        :items="docStore.documents"
        height="320"
        item-height="48"
        >
            <template v-slot:default="{ item }">
                <v-list-item
                :active="docStore.currentDocument.id == item.id"
                :value="item.id"
                :title="item.title"
                :subtitle="item.published"
                color="primary"
                prepend-icon="mdi-file-document"
                >
                    <template v-slot:append>
                        <v-tooltip
                        location="bottom"
                        >
                            <template v-slot:activator="{ props }">
                                <v-btn
                                v-bind="props"
                                type="button"
                                icon="mdi-information-outline"
                                size="small"
                                class="mr-1"
                                @click="selectItem(item)"></v-btn>
                            </template>

                            <span>Details</span>
                        </v-tooltip>

                        <v-tooltip
                        location="bottom"
                        >
                            <template v-slot:activator="{ props }">
                                <v-btn
                                v-bind="props"
                                icon="mdi-delete-outline"
                                size="small"
                                type="button"
                                @click="openDialog(item)">
                                </v-btn>

                                <v-dialog
                                v-model="confirmDialog.isActive"
                                width="auto"
                                opacity="0.1"
                                >
                                    <v-card
                                    max-width="400"
                                    elevation="0"
                                    >
                                        <v-card-title>
                                            Remove document
                                        </v-card-title>

                                        <v-card-subtitle>
                                            <p>#id: {{ confirmDialog.item.id }}</p>
                                            <p>#title: {{ confirmDialog.item.title }}</p>
                                            <p>#published: {{ confirmDialog.item.published }}</p>
                                        </v-card-subtitle>

                                        <v-card-text>
                                            <p>Are you shure that you want remove this document?</p>
                                        </v-card-text>

                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn type="button" @click="acceptDialog">Yes</v-btn>
                                            <v-btn type="button" @click="refuseDialog">No</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>
                            </template>

                            <span>Delete</span>
                        </v-tooltip>
                    </template>
                </v-list-item>
            </template>
        </v-virtual-scroll>

        <v-btn
        class="w-100"
        @click="docStore.loadDocuments"
        >
            Load more
        </v-btn>
    </v-card>
</template>

<style scoped></style>
