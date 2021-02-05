<template>
  <div class="receita">
    <h1>{{ receita.receita }}</h1>
    <v-card class=introducao>{{ receita.introducao }}</v-card>

    <h2>Ingredientes</h2>
    <div class="ingredientes">

      <v-card class="card_ingredientes">
        <li v-for="ingredientes in lista_i" :key="ingredientes">
          <span>{{ ingredientes }}</span>
        </li>
      </v-card>

      <v-card>
        <v-img class="imagem"
          :src="receita.foto"
          height="300px"
          width="450px">
        </v-img>
      </v-card>
      
    </div>

    <h2>Modo de Preparo</h2>
      <v-card class="card_preparo" margin="50px">
        <p class="preparo_indice" v-for="(preparo, index) in lista_p" :key="preparo">
          {{index + 1}}.
          <span class="preparo">
            {{preparo}}
          </span>
        </p><br>
      </v-card>
    <h3>Autor: {{ receita.autor }}</h3>

  </div>
</template>

<script>
import AppApi from "~apijs";

export default {
  props: ["posts"],
  asyncData(context) {
    return {
      receita: context.params.receita,
    };
  },
  methods: {
    formatacao(texto) {
      texto = texto.split("- ");
      texto.splice(0, 1);
      return texto;
    },
  },
  data() {
    return{
      lista_i: [],
      lista_p: [],
    }
  },
  mounted() {
    this.lista_i = this.formatacao(this.receita.ingredientes);
    this.lista_p = this.formatacao(this.receita.preparo);
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Sofia');

.receita {
  font-family: 'Sofia', sans-serif;
  font-size: 20px;
}
.introducao{
  display: flex;
  text-align: center;
  margin: 50px 150px !important;
  padding: 20px;
}
.ingredientes {
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin-bottom: 30px;
}
.preparo_indice {
  display: flex;
  color: #bb4b00;
  font-weight: bold;
  font-size: 40px;
}
.preparo {
  display: flex;
  text-align: justify;
  align-items: center;
  margin-left: 10px;
  color: black;
  font-weight: normal;
  font-size: 20px;
}
.card_ingredientes {
  display: block;
  padding: 30px;
}
.card_preparo {
  display: block;
  padding: 30px 30px 0px 30px;
  margin: 30px 150px !important;
}
.theme--light.v-sheet {
  background-color: #e9d7ca;
  border-radius: 20px;
  margin: 50px;
}
h1, h2 {
  text-align: center;
}
h3 {
  text-align: right;
}

@media only screen and (max-width: 700px) {
    .introducao{
      margin: 5px 15px !important;
    }
    .v-image__image {
      height: 100%;
      width: 150%; 
    }
    .elemen.style {
      height: 100%;
      width: 150%; 
    }
  }

</style>
