<template>
    <div class="statbar" ref="statbar"> 
        <div class="name">{{this.statName}}</div>
        <div class="value" ref="value">{{this.statValue}}</div>
        <div class="barContainer">
            <div class="bar" ref="bar">
            </div>
        </div>
    </div>
</template>

<script>
import { gsap } from "gsap"
export default {
    props: ["stat"],
    data() {
        return {
            statName: null,
            statValue: 0,
        }
    },
    methods: {
        shortenName(name) {
            switch(name) {
                case "attack":
                    this.statName = "ATK"
                    break
                case "defence":
                    this.statName = "DEF"
                    break
                case "hp":
                    this.statName = "HP"
                    break
                case "specialAttack":
                    this.statName = "S.ATK"
                    break
                case "specialDefence":
                    this.statName = "S.DEF"
                    break
                case "speed":
                    this.statName = "SPD"
                    break;
            }
        }
    },
    mounted() {
        this.shortenName(this.$props.stat.key)
        this.statValue = this.$props.stat.value
        let bar = this.$refs.bar
        gsap.fromTo(bar, {width: "10%"}, {width: this.statValue + "%", duration: 1, ease: "expo", delay: 0.5})
    }
}
</script>

<style scoped>
.statbar{
    display: inline;
}

.name {
    /* border: 1px solid blue; */
    width: 20%;
    height: 2.5vh;
    margin-left: 0%;
    text-align: right;
    float: left;
}
.barContainer{
    position:relative;
    /* border: 1px solid green; */
    width: 75%;
    height: 75%;
    left: 23%;
    top: 5%;
}
.bar {
    /* border: 1px solid purple; */
    height: 100%;
    width: 10%;
    background-color: #cf4444;
    border-radius: 1.25vh;
    color: #ffffff;
    z-index: 1;
}
.value {
    /* border: 1px solid orange; */
    height: 100%;
    width: 10%;
    text-align: left;
    position: relative;
    text-align: center;
    left: 5%;
    float: left;
    z-index: 2;
    color: #ffffff;
    margin-top: 0.75%;
}
</style>