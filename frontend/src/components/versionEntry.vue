<template>
  <button class="entry" ref="entry" @click="queryVersion"
  v-bind:style='{ backgroundImage : `url(${image})` }'>
    <!-- <img :src="getImgPath"/> -->
  </button>
</template>

<script>
export default {
  props: ["data", "keyVersions", "selected"],
  data() {
    return {
        image : require("../assets/" + this.$props.data.name.replace(/\s/g, "")+ ".png"),
    };
  },
  updated() {},
  methods: {
    queryVersion() {
      this.$emit("queryVersion", this.$props.data.version_id);
    },
  },
  mounted() {
    let button = this.$refs.entry;
    // let name = this.$props.data.name.replace(/\s/g, "");
    // button.style.backgroundImage = "url('" + name + ".png')";
    if (this.data.version_id == this.$props.selected) {
      button.style.border = "3px solid #000000";
    }
  },
  computed: {
    getImgPath() {
      let images = require.context("../assets/", false, /\.png$/);
      let name = this.$props.data.name.replace(/\s/g, "");
      return images("./" + name + ".png");
    },
  },
};
</script>

<style scoped>
.versionEntryContainer {
  height: 12vh;
  width: 18vw;
  float: left;
}
.entry {
  height: 12vh;
  width: 18vw;
  float: left;
  background-color: #ffffff00;
  margin-right: 0%;
  transition: border-color 0.3s;
  border: 0px solid rgb(255, 255, 255);
  border-radius: 2.5vw;
  background-image: url("../assets/blue.png");
  background-size: 100% 100%;
}
.entry:hover {
  cursor: pointer;
  border: 2px solid #cf4444;
}
</style>