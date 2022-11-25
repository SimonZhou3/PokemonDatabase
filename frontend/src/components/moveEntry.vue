<template>
    <div class="moveContainer" ref="moveContainer">
        <div class="moveData" id="desc"> {{this.$props.moveData.type_id}}</div>
        <div class="moveData" id="accuracy">accuracy: {{this.$props.moveData.accuracy}}</div>
        <div class="moveData" id="damageClass">damage_class: {{this.$props.moveData.damage_class}}</div>
        <div class="moveData" id="effectChance">effect_chance: {{this.$props.moveData.effect_chance}}</div>
        <div class="moveData" id="power">power: {{this.$props.moveData.power}}</div>
        <div class="moveData" id="pp">pp: {{this.$props.moveData.pp}}</div>
        <div class="moveData" id="priority">priority: {{this.$props.moveData.priority}}</div>
    </div>
</template>

<script>
export default {
    props:["moveData"],
    data() {
        return {
        }
    },
    // mounted() {
    //     this.accuracy = this.$props.acc
    // }
}
</script>

<style scoped>
.moveContainer {
    border: 1px solid orange;
    width: 90%;
    display:flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
}
.moveData{
    border: 1px solid blue;
}
</style>