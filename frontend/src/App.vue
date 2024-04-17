<script setup>
import UploadFormComponent from './components/UploadFormComponent.vue';
import DocumentsListComponent from './components/DocumentsListComponent.vue';
import DocumentDetailComponent from './components/DocumentDetailComponent.vue';
import WordsTableComponent from './components/WordsTableComponent.vue';
</script>

<template>
    <v-app>
        <v-container fluid class="fill-height px-0 py-0">
            <v-row class="fill-height" no-gutters>
                <v-col cols="3">
                    <v-container fluid>
                        <v-row>
                            <v-col>
                                <UploadFormComponent/>
                            </v-col>
                        </v-row>

                        <v-row>
                            <v-col>
                                <DocumentsListComponent/>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-col>

                <v-col cols="9">
                    <v-container fluid>
                        <v-row>
                            <v-col>
                                <DocumentDetailComponent/>
                            </v-col>
                        </v-row>

                        <v-row >
                            <v-col>
                                <WordsTableComponent/>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<style scoped></style>
