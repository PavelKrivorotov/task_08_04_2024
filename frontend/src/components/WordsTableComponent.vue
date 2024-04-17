<script setup>
import { reactive } from 'vue';

import { useDocumentWordStore } from '@/pinia/document-word-store';
const wordStore = useDocumentWordStore()

const headers = [
    {title: 'Word', key: 'word'},
    {title: 'Tf', key:'tf'},
    {title: 'Idf', key:'idf'}
]
const itemsPerPageOptions = reactive([]);
</script>

<template>
    <v-card>
        <v-card-title>
            Words of the document
        </v-card-title>

        <v-card-text>
            <v-data-table-server
            v-model:items-per-page="wordStore.countWordsPerPage"
            :headers="headers"
            :items-per-page-options="itemsPerPageOptions"
            :items="wordStore.words"
            :items-length="wordStore.countWords"
            :loading="wordStore.loading"
            @update:options="wordStore.loadWords"
            >
                <template v-slot:headers="{ columns }">
                    <tr>
                        <template v-for="column in columns" :key="column.key">
                        <th class="font-weight-bold th-width">
                                {{ column.title.toUpperCase() }}
                        </th>
                    </template>
                    </tr>
                </template>
            </v-data-table-server>
        </v-card-text>
    </v-card>
</template>

<style scoped>
.th-width {
    width: 33%;
}
</style>
