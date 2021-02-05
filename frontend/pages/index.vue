<template>
  <home :posts="posts"></home>
</template>

<script>

import home from '~/components/Home.vue'
import AppApi from '~apijs'

export default {
  components: {
    home
  },
  asyncData() {
    return AppApi.list_posts().then(result => {
      return {
        posts: result.data
      }
    })
  },
  data () {
    return {
      posts: null,
    }
  }
}
</script>

<style>
</style>