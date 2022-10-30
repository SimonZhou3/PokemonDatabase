<script>
</script>

<template>
  <div class="about flex-column justify-content-center">
    <h1 class="d-flex justify-content-center">Search for a Pokemon</h1>
    <div class="d-flex justify-content-center">
    <vue3-simple-typeahead
        id="typeahead_id"
        placeholder="Start writing..."
        :items="['One','Two','Three']"
        :minInputLength="1"
        :itemProjection="itemProjectionFunction"
        @selectItem="selectItemEventHandler"
        @onInput="onInputEventHandler"
        @onFocus="onFocusEventHandler"
        @onBlur="onBlurEventHandler"
    >
    </vue3-simple-typeahead>
      </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
