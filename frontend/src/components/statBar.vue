<template>
  <div class="statbar" ref="statbar">
    <div class="name">{{ this.statName }}</div>
    <div class="barContainer">
        <div class="value" ref="value">{{ this.statValue }}</div>
      <div class="bar" ref="bar">
      </div>
    </div>
  </div>
</template>

<script>
import { gsap } from "gsap";
export default {
  props: ["stat", "color"],
  data() {
    return {
      statName: null,
      statValue: 0,
      accentColor: this.$props.color,
    };
  },
  methods: {
    shortenName(name) {
      switch (name) {
        case "attack":
          this.statName = "ATK";
          break;
        case "defence":
          this.statName = "DEF";
          break;
        case "hp":
          this.statName = "HP";
          break;
        case "specialAttack":
          this.statName = "S.ATK";
          break;
        case "specialDefence":
          this.statName = "S.DEF";
          break;
        case "speed":
          this.statName = "SPD";
          break;
      }
    },
  },
  mounted() {
    this.shortenName(this.$props.stat.key);
    this.statValue = this.$props.stat.value;
    let bar = this.$refs.bar;
    let width;
    if (this.statValue > 100) {
      width = 100;
    } else {
      width = this.statValue;
    }
    gsap.fromTo(
      bar,
      { width: "10%" },
      { width: width + "%", duration: 1, ease: "expo", delay: 0.5 }
    );
  },
};
</script>

<style scoped>
.statbar {
  display: inline;
}

.name {
  border: 1px solid blue;
  width: 10%;
  height: 2.5vh;
  margin-left: 0%;
  text-align: right;
  float: left;
  font-weight: bold;
  overflow: hidden;
  color: #707070;
}
.barContainer {
  position: relative;
  border: 1px solid green;
  width: 90%;
  height: 75%;
  left: 12%;
  top: 5%;
}
.bar {
  border: 1px solid purple;
  height: 100%;
  width: 10%;
  background-color: v-bind(accentColor);
  border-radius: 1.25vh;
  color: #ffffff;
  z-index: 1;
    box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
}
.value {
  position: absolute;
  border: 1px solid orange;
  height: 75%;
  width: 10%;
  text-align: left;
  position: relative;

  left: -10%;
  float: left;
  z-index: 2;
  color: #ffffff;
  font-weight: bold;
}
</style>