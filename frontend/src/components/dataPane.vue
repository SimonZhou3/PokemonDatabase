<template>
    <div class= "pane" ref="pane">
        <div class="dataContainer" id="version">Version
        </div>
        <div class="dataContainer" id="move">Move
        </div>
        <div class="dataContainer" id="area">Area
        </div>
        <div class="dataContainer" id ="item">item
        </div>
    </div>
</template>

<script>
import { gsap } from "gsap"
export default {
    data() {
        return {

        }
    },
    mounted() {
        console.log("showing data")
        let pane = this.$refs.pane
        pane.style.opacity = 1
        gsap.fromTo(pane, {top: "50vh"}, {top: "15vh", duration: 1, ease: "expo"})
    }
}
</script>

<style scoped>
.pane {
    position: relative;
    width: 90vw;
    height: 65vh;
    left: 5vw;
    background-color: #ffffff;
    border-radius: 5vh;
    opacity: 0;
    transition: opacity 1s;
box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    /* filter: drop-shadow(0px 0px 6px #ebebeb) */
}
.dataContainer {
    position: relative;
    border: 1px solid red;
    left: 0%;
    width: 30%;
    height: 50vh;
    display: inline-block;
    margin-right: 1%;
    overflow: auto;
}
.dataContainer#version {
    margin-top: 2vh;
    width: 93%;
    height: 10vh;
}
</style>