<template>
  <button class="entry" ref="entry" @click="queryPokemon">{{this.$props.pokemon.name}}</button>
</template>

<script>
export default {
  props: ["pokemon"],
  data() {
    return {};
  },
  updated() {},
  methods: {
    queryPokemon() {
      this.$emit("querying");
      //send request to back end
      fetch("http://127.0.0.1:5000/pokemon/"+this.$props.pokemon.pokemon_id, {
      method: "GET",
    }
    ).then((response) => response.json())
    .then((data) => this.onResponse(data))
    },
    onResponse(data) {
      console.log("received data from backend")
      this.$emit("response", data)
    }
  },
};
</script>

<style scoped>
.entry {
  height: 5vh;
  background-color: #ffffff00;
  margin-bottom: 1vh;
  width: 95%;
  border-radius: 2.5vh;
  border: 0;
  transition: background-color 0.3s;
}
.entry:hover {
  background-color: #cf4444;
}
</style>