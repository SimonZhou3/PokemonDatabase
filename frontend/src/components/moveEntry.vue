<template>
    <div class="moveContainer" ref="moveContainer">
        <div class="moveData" id="desc"> {{this.$props.moveData.type_id}}</div>
        <div class="moveData" id="accuracy"><b>accuracy:</b> {{this.$props.moveData.accuracy}}</div>
        <div class="moveData" id="damageClass"><b>damage_class:</b> {{this.$props.moveData.damage_class}}</div>
        <div class="moveData" id="effectChance"><b>effect_chance:</b> {{this.$props.moveData.effect_chance}}</div>
        <div class="moveData" id="power"><b>power:</b> {{this.$props.moveData.power}}</div>
        <div class="moveData" id="pp"><b>pp:</b> {{this.$props.moveData.pp}}</div>
        <div class="moveData" id="priority"><b>priority:</b> {{this.$props.moveData.priority}}</div>
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