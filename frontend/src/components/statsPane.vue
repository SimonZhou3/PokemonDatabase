<template>
  <div class="pane" ref="pane">
    <div v-for="stat of statList" :key="stat" class="bar">
      <statBar :stat="stat" :color="this.$props.color" />
    </div>
  </div>
</template>

<script>
import { gsap } from "gsap";
import statBar from "./statBar.vue";
export default {
  props: ["stats", "color", "toggle"],
  watch: {
    toggle: function (value) {
      if (value) {
        let pane = this.$refs.pane;
        gsap.to(pane, { left: "-40vw", duration: 0.5, ease: "expo" });
      }
    },
  },
  components: {
    statBar,
  },
  data() {
    return {
      statList: [],
    };
  },
  mounted() {
    for (let stat in this.$props.stats) {
      this.statList.push({ key: stat, value: this.$props.stats[stat] });
    }
    console.log("showing stats");
    let pane = this.$refs.pane;
    pane.style.opacity = 1;
    gsap.fromTo(
      pane,
      { left: "-25vw" },
      { left: "5vw", duration: 1, ease: "expo", delay: 0.3 }
    );
  },
  // updated() {
  //     console.log("updating stats pane", this.reset)
  //     if (this.reset) {
  //         let pane = this.$refs.pane
  //         gsap.to(pane, {left: "-25vw", duration: 1, ease:"expo"})
  //     }
  // }
};
</script>

<style scoped>
.pane {
  position: absolute;
  width: 25vw;
  height: 25vh;
  top: 5vh;
  background-color: #ffffff;
  border-radius: 5vh;
  padding: 1%;
  opacity: 0;
  transition: opacity 1s;
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
  /* filter: drop-shadow(0px 0px 3px #ebebeb) */
}
.bar {
  /* border: 1px solid red; */
  height: 10%;
  width: 100%;
  margin-top: 1.3vh;
}
</style>