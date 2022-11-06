import { createApp } from "vue";
import { createPinia } from "pinia";
import 'bootstrap-vue';
import 'bootstrap';
import SimpleTypeahead from 'vue3-simple-typeahead';

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(SimpleTypeahead);
app.mount("#app");
