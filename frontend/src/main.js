import { createApp } from 'vue'
import App from './App.vue'

import { createPinia } from 'pinia'
import { vuetify } from './vuetify'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(vuetify)

app.mount('#app')
