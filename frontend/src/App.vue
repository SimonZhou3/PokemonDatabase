<template>
  <div id="nav">
    <trainer-nav-bar/>
  </div>
  <router-view/>
</template>

<script>
import TrainerNavBar from "@/views/trainerNavBar";
export default {
  components: {TrainerNavBar}
}
</script>