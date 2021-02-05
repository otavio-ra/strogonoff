<template>
    <div>
        <v-layout row>
            <v-flex class="card">
                <v-card v-for="post in posts" :key="post.id">
                    <v-img
                        :src="post.foto"
                        height="200px"
                        width="300px">
                    </v-img>
            
                    <v-card-title class="card_timeline" primary-title>
                        <div>
                            <div class="headline">{{post.receita}}</div>
                            <span two-line class="grey--text"></span>
                        </div>
                    </v-card-title>
                    <v-spacer color="white"></v-spacer>
            
                    <v-card-actions class="card_timeline" >
                        <v-btn class="botao" flat dark ripple color="#bb4b00" :to="{name: 'receita', params: {receita: post}}">Confira a receita</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>

export default {
  props: ['posts'],

  data (){
      console.log(this.posts)
    return {}
    }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Sofia');

.card {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.headline {
    font-family: 'Sofia', sans-serif !important;
    line-break: auto;
    max-width: 270px;
    text-align: center;
}
.card_timeline {
    justify-content: center;
    background-color: #e9d7ca;
    height: 11vh;
}
.theme--light.v-sheet {
    border-radius: 20px;
    margin: 50px;
}
</style>
