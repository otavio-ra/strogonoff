<template>
  <!-- <timeline :tweets="tweets"></timeline> -->
  <timeline :posts="posts"></timeline>
</template>

<script>

import timeline from '~/components/Timeline.vue'

export default {
    // props: ['tweets'],
    props: ['posts'],
    components: {
        timeline
    },
  data () {
    return {}
  }
}
</script>

<style>
</style>