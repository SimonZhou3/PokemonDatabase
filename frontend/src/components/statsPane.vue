<template>
    <div class = "pane" ref="pane">Stat
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
        console.log("showing stats")
        let pane = this.$refs.pane
        pane.style.opacity = 1
        gsap.fromTo(pane, {left: "-25vw"}, {left: "5vw", duration: 1, ease: "expo", delay: 0.3})
    }
}
</script>

<style scoped>
.pane {
    position: relative;
    width : 25vw;
    height: 25vh;
    top: -80vh;
    background-color: #ffffff;
    border-radius: 5vh;
    opacity: 0;
    transition: opacity 1s;
    
    
    box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
    /* filter: drop-shadow(0px 0px 3px #ebebeb) */
}
</style>