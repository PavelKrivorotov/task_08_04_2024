<script setup>
import { useDocumentStore } from '@/pinia/document-store';
const docStore = useDocumentStore()
</script>

<template>
    <v-card>
        <v-card-title>
            Document
        </v-card-title>

        <v-card-text>
            <v-row>
                <v-col>
                    <v-text-field
                    label="UUID"
                    v-model="docStore.currentDocument.id"
                    readonly
                    ></v-text-field>

                    <v-text-field
                    label="Title"
                    v-model="docStore.currentDocument.title"
                    readonly
                    ></v-text-field>
                </v-col>

                <v-col>
                    <v-text-field
                    label="Published"
                    v-model="docStore.currentDocument.published"
                    readonly
                    ></v-text-field>

                    <v-text-field
                    label="Count of words"
                    v-model="docStore.currentDocument.countWords"
                    readonly
                    ></v-text-field>
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<style scoped></style>
