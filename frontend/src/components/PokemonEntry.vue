<template>
  <button class="entry" ref="entry" @click="queryPokemon">
    {{ this.$props.pokemon.name }}
  </button>
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
      this.$emit("querying", this.$props.pokemon.pokemon_id);
      //send request to back end
      // fetch("http://127.0.0.1:5000/pokemon/" + this.$props.pokemon.pokemon_id, {
      //   method: "GET",
      // })
      //   .then((response) => response.json())
      //   .then((data) => this.onResponse(data));
    },
    async querySpecificPokemons(versions) {
      let filteredVersion = this.filterVersions(versions);
      console.log(filteredVersion);
      let pokemonVersionData = {};
      for (let version of filteredVersion) {
        fetch(
          "http://127.0.0.1:5000/pokemon/" +
            this.$props.pokemon.pokemon_id +
            "?version_id=" +
            version.version_id,
          {
            method: "GET",
          }
        )
          .then((response) => response.json())
          .then((data) => {
            pokemonVersionData[data.data[0].pokemon_version_id] = data;
            console.log(pokemonVersionData, data.data[0].pokemon_version_id);
            if (
              data.data[0].pokemon_version_id ==
              filteredVersion[filteredVersion.length - 1].version_id
            ) {
              console.log("retrieved all version data");
            }
          });
      }
    },
    async fetchVerisonData(dataGeneric, versions) {
      let versionData = {};
      let filteredList = this.filterVersions(versions);
      for (let version of filteredList) {
        versionData[version.version_id] = null;
      }
      let firstVersion = filteredList.shift();
      versionData[firstVersion.version_id] = await fetch(
        "http://127.0.0.1:5000/pokemon/" +
          this.$props.pokemon.pokemon_id +
          "?version_id=" +
          firstVersion.version_id,
        {
          method: "GET",
        }
      ).then((response) => response.json())
      .then((data)=>this.onResponseSpecific(dataGeneric,data))
        // .then((response) => response.json())
        // .then(this.$emit("response", dataGeneric, versionData))
        // .then(() => {
        //   for (let version of filteredList) {
        //     fetch(
        //       "http://127.0.0.1:5000/pokemon/" +
        //         this.$props.pokemon.pokemon_id +
        //         "?version_id=" +
        //         version.version_id,
        //       {
        //         method: "GET",
        //       }
        //     )
        //       .then((response) => response.json())
        //       .then((data) => {
        //         versionData[data.data[0].pokemon_version_id] = data;
        //       });
        //   }
        // });
    },
    onResponseSpecific(genericData, versionData) {
      // console.log(versionData.data[0])
      this.$emit("response", genericData, versionData)
    },
    async onResponse(dataGeneric) {
      console.log("received data from backend");
      let versions = dataGeneric.data[0].version_list;
      let filteredVersion = this.filterVersions(versions)
      this.$emit("response", dataGeneric, filteredVersion)
      // this.fetchVerisonData(dataGeneric, versions);
      // this.querySpecificPokemons(versions).then(() => {
      //   // console.log(this.pokemonVersionData);
      // });
    },
    filterVersions(versions) {
      let filteredVersion = [];
      for (let version of versions) {
        if (
          version.name == "red" ||
          version.name == " yellow" ||
          version.name == "gold" ||
          version.name == "crystal" ||
          version.name == "ruby" ||
          version.name == "emerald" ||
          version.name == "firered" ||
          version.name == "diamond" ||
          version.name == "platinum" ||
          version.name == "heartgold" ||
          version.name == "black" ||
          version.name == "black 2"
        ) {
          filteredVersion.push(version);
        }
      }
      return filteredVersion;
    },
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
  font-weight: bold;
}
.entry:hover {
  background-color: #cf4444;
  cursor: pointer;
}
</style>