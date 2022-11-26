<template>
  <div class="dataContainer" ref="dataContainer">
    <button class="entry" ref="entry" @click="queryData">
      {{ this.dataName }}
    </button>
    <div class="moveEntryContainer">
      <moveEntry :moveData="this.moveData" :color="this.$props.color" v-if="this.showMove" />
    </div>
    <div class="entryContainer">
      <itemEntry :itemData="this.itemData" :color="this.$props.color" v-if="this.showItem" />
    </div>
  </div>
</template>

<script>
import { gsap } from "gsap";
import moveEntry from "./moveEntry.vue";
import itemEntry from "./itemEntry.vue";
export default {
  props: ["data", "color", "type"],
  components: {
    moveEntry,
    itemEntry,
  },
  data() {
    return {
      accentColor: this.$props.color.accent,
      accentText: this.$props.color.text_accent,
      dataName: null,
      showMove: false,
      moveData: null,
      showArea: false,
      areaData: null,
      showItem: false,
      itemData: null,
    };
  },
  updated() {},
  mounted() {
    // console.log(this.$props.data, this.$props.type)
    switch (this.$props.type) {
      case "Move":
        this.dataName = this.$props.data.name;
        break;
      case "Area":
        this.dataName = this.$props.data.area_name;
        break;
      case "Item":
        this.dataName = this.$props.data.name;
        break;

      default:
        break;
    }
  },
  methods: {
    displayData(data) {
      switch (this.$props.type) {
        case "Move":
          this.moveData = data.data[0];
          this.showMove = true;
          break;
        case "Area":
          this.areaData = data.data[0];
          this.showArea = true;
          break;
        case "Item":
          this.itemData = data.data[0];
          this.showItem = true;
          break;
      }
      this.received = true;
      let container = this.$refs.dataContainer;
      // let entry = this.$refs.entry
      container.style.color = this.accentText
      // entry.style.color="#ffffff"
      gsap.to(container, { backgroundColor: this.accentColor});
      console.log(data);
      // let dataContainer = this.$refs.dataContainer;
      // gsap.to(dataContainer, { height: "40vh", duration: 0.5, ease: "expo" });
    },
    queryData() {
      if (!this.showMove && !this.showArea && !this.showItem) {
        console.log("querying " + this.dataName);
        if (this.$props.type == "Move") {
          fetch("http://127.0.0.1:5000/move/" + this.$props.data.move_id, {
            method: "GET",
          })
            .then((response) => response.json())
            .then((data) => this.displayData(data));
        } else if (this.$props.type == "Area") {
          console.log("querying " + this.dataName);
        } else if (this.$props.type == "Item") {
          console.log("querying " + this.dataName);
          fetch("http://127.0.0.1:5000/item/" + this.$props.data.item_id, {
            method: "GET",
          })
            .then((response) => response.json())
            .then((data) => this.displayData(data));
        }
      } else {
        this.showMove = false;
        this.showArea = false;
        this.showItem = false;
        let container = this.$refs.dataContainer;
        gsap.to(container, { backgroundColor: "#ffffff" });
              let entry = this.$refs.entry
      entry.style.color="#2c3e50"
      }
      // this.$emit("queryData", this.$props.data, this.$props.type)
    },
  },
};
</script>

<style scoped>
.entry {
  height: 5vh;
  background-color: #ffffff00;
  margin-top: 1vh;
  margin-bottom: 1vh;
  margin-left: auto;
  margin-right: auto;
  width: 95%;
  border-radius: 2.5vh;
  border: 0;
  transition: background-color 0.3s;
  font-weight: bold;
  font-size: 30px;
}
.entry:hover {
  cursor: pointer;
  background-color: v-bind(accentColor);
  color: v-bind(accentText)
}
.dataContainer {
  /* border: 1px solid green; */
  width: 90%;
  border-radius: 2.5vh;
  display: flex;
  flex-direction: column;
  transition: height 1s;
}
.dataEntry {
  /* border: 1px solid red; */
  width: 100%;
  height: 30vh;
}
/* .moveEntryContainer {
  display: flex;
  flex-direction: column;
} */
</style>