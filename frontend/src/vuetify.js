import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css'

import { createVuetify } from 'vuetify';

import { VApp } from 'vuetify/components/VApp';
import { VContainer, VRow, VCol, VSpacer } from 'vuetify/components/VGrid';
import { VForm } from 'vuetify/components/VForm';
import { VFileInput } from 'vuetify/components/VFileInput';
import { VTextField } from 'vuetify/components/VTextField';
import { VBtn } from 'vuetify/components/VBtn';
import { VListItem } from 'vuetify/components/VList';
import { VDataTableServer } from 'vuetify/components/VDataTable';
import { VCard, VCardTitle, VCardSubtitle, VCardText, VCardActions } from 'vuetify/components/VCard';
import { VTooltip } from 'vuetify/components/VTooltip';
import { VDivider } from 'vuetify/components/VDivider';
import { VVirtualScroll } from 'vuetify/components/VVirtualScroll';
import { VDialog } from 'vuetify/components/VDialog';

export const vuetify = createVuetify({
    icons: {
        defaultSet: 'mdi'
    },
    components: {
        VApp,

        VContainer,
        VRow,
        VCol,
        VSpacer,

        VForm,
        VFileInput,
        VTextField,

        VBtn,

        VListItem,

        VDataTableServer,

        VCard,
        VCardTitle,
        VCardSubtitle,
        VCardText,
        VCardActions,

        VTooltip,

        VDivider,
        VVirtualScroll,

        VDialog,
    }
})

