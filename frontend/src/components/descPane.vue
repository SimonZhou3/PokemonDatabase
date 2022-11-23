<template>
  <div class="pane" ref="pane">
    <div class="block" id="name" ref="name">{{this.$props.name}}</div>
    <div class="block" id="types" ref="types">
        <div v-for="type of this.$props.types" :key=type class="typeIcon">{{type.type}}
        </div>
    </div>
    <div class="block" id="desc" ref="desc">{{this.$props.description}}</div>
  </div>
</template>

<script>
import {gsap} from "gsap"
export default {
  props: ["types", "name", "description"],
  data() {
    return {};
  },
  mounted() {
    let pane = this.$refs.pane;
    pane.style.opacity = 1;
    gsap.fromTo(
      pane,
      { left: "125vw" },
      { left: "68vw", duration: 1, ease: "expo", delay: 0.3 }
    );
  },
};
</script>

<style scoped>
.pane {
  position: relative;
  width: 25vw;
  height: 25vh;
  top: -108.5vh;
  background-color: #ffffff;
  border-radius: 5vh;
  padding: 1%;
  opacity: 0;
  transition: opacity 1s;
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
  font-size: 30px;
  /* filter: drop-shadow(0px 0px 3px #ebebeb) */
}
.block {
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 1%;
    width: 90%;
    height: 20%;
    border: 1px solid red
}
.block#name {
    height: 10%;
    font-weight: bold;
}
.block#desc{
    height: 70%;
    overflow:auto;
}
.typeIcon{
    width: 30%;
    height: 100%;
    border: 1px solid blue;
}
/* width */
::-webkit-scrollbar {
  width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #ffffff;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #cf4444;
  border-radius: 2.5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: rgb(255, 77, 77);
}
</style>