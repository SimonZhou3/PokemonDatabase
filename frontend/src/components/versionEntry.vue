<template>
  <button class="entry" ref="entry" @click="queryVersion"
  :style="{'background-image':versionImg}">
    <!-- <img :src="getImgPath"/> -->
  </button>
</template>

<script>
export default {
  props: ["data"],
  data() {
    return {
        versionImg: null,
    };
  },
  updated() {},
  methods: {
    queryVersion() {
      console.log("querying " + this.$props.data.name);
    },
  },
  mounted() {
    let name = this.$props.data.name.replace(/\s/g, '');
    let button = this.$refs.entry
    button.style.backgroundImage = "url('" + name + ".png')"
  },
  computed: {
    getImgPath() {
        let images = require.context('../assets/', false, /\.png$/)
        let name = this.$props.data.name.replace(/\s/g, '');
        return images('./' + name + ".png")
    }
  }
};
</script>

<style scoped>
.entry {
  height: 9vh;
  background-color: #ffffff00;
  margin-right: 0%;
  width: 10vw;
  border-radius: 2.5vh;
  transition: border-color 0.3s;
  border: 1px solid green;
  display: inline;
  background-image: url("../assets/blue.png");
  background-size: 100% 100%;
}
.entry:hover {
  cursor: pointer;
  border: 2px solid #cf4444;
}
</style>