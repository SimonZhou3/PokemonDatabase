<template>
  <div class="pane" ref="pane">
    <div class="block" id="name" ref="name">{{this.$props.name}}</div>
    <div class="block" id="types" ref="types">
        <div v-for="type of this.$props.types" :key=type class="typeIcon"
        v-bind:style="{
            backgroundImage: `linear-gradient(to right, ` +
            this.$props.colors[type.type].main + ', ' +
            this.$props.colors[type.type].accent + ')' ,
            color: this.$props.colors[type.type].text_accent
            }"
        >{{type.type}}
        </div>
    </div>
    <div class="block" id="desc" ref="desc">{{this.$props.description}}</div>
  </div>
</template>

<script>
import {gsap} from "gsap"
export default {
  props: ["types", "name", "description", "colors", "toggle"],
  watch: {
    toggle: function(value) {
      if(value) {
        let pane = this.$refs.pane
        gsap.to(pane, {left: "100vw", duration: 0.5, ease: "expo"})
      }
    }
  },
  data() {
    return {
      accentColor : this.$props.colors[this.$props.types[0].type]["accent"]
    };
  },
  mounted() {
    let pane = this.$refs.pane;
    console.log(this.accentColor)
    pane.style.opacity = 1;
    gsap.fromTo(
      pane,
      { left: "125vw" },
      { left: "70vw", duration: 1, ease: "expo", delay: 0.3 }
    );
  },
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
  font-size: 30px;
  overflow: hidden;
  /* filter: drop-shadow(0px 0px 3px #ebebeb) */
}

.block {
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 1%;
    width: 90%;
    height: 20%;
    /* border: 1px solid red */
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
    position: relative;
    top: 20%;
    width: 30%;
    height: 80%;
    /* border: 1px solid blue; */
    border-radius: 2.5vh;
    display: inline-block;
    line-height: normal;
    vertical-align: middle;
    text-align: center;
    color: #ffffff;
    margin-left: 2%;
    font-size: 3vh;
    font-weight: bold;
      box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
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
  background: v-bind(accentColor);
  border-radius: 2.5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: v-bind(accentColor);
}
</style>