import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/index";
import { Collapse, CollapseItem } from "vant";
// 2. Import the components style
import "vant/lib/index.css";
const app = createApp(App);
app.use(router);
app.use(Collapse);
app.use(CollapseItem);
app.mount("#app");
