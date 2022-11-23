<template>
  <button
    class="entry"
    ref="entry"
    @click="queryVersion"
    v-bind:style="{ backgroundImage: `url(${image})` }"
  >
    <!-- <img :src="getImgPath"/> -->
  </button>
</template>

<script>
import { gsap } from "gsap";
export default {
  props: ["data", "keyVersions", "selected", "color"],
  data() {
    return {
      image: require("../assets/" +
        this.$props.data.name.replace(/\s/g, "") +
        ".png"),
        accentColor: this.$props.color
    };
  },
  updated() {},
  methods: {
    queryVersion() {
      this.$emit("queryVersion", this.$props.data.version_id);
      this.loadAnimation();
    },
    loadAnimation() {
      if (this.data.version_id != this.$props.selected) {
        let icon = this.$refs.entry;
        gsap.to(icon, { y: -20, duration: 0.5, ease: "expo",delay:0.5 });
        gsap.to(icon, {
          y: 0,
          duration: 0.5,
          ease: "bounce",
          delay: 1,
          onComplete: this.loadAnimation,
        });
      }
    },
  },
  mounted() {
    let button = this.$refs.entry;
    // let name = this.$props.data.name.replace(/\s/g, "");
    // button.style.backgroundImage = "url('" + name + ".png')";
    if (this.data.version_id == this.$props.selected) {
      button.style.border = "3px solid "+this.accentColor;
    }
  },
  computed: {
  },
};
</script>

<style scoped>

.entry {
  margin-top: 15%;
  height: 12vh;
  width: 10vw;
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
  border: 2px solid v-bind(accentColor);
}
</style>