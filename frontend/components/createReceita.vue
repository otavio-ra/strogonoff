<template>
  <v-dialog scrollable v-model="visible" class="modal" max-width="1000px">
    <v-card>
      <v-card-title class="title"><strong>ADICIONE UMA RECEITA</strong></v-card-title>
      <v-card-text>
        <v-container>

          <v-card-subtitle class="subtitle"> Título da Receita:
            <v-textarea class="input_add_receita" rows="1" label="Título da receita" required v-model="receita" />
          </v-card-subtitle>

          <v-card-subtitle class="subtitle"> Introdução:
            <v-textarea class="input_add_receita" rows="1" label="Introdução" required v-model="introducao" />
          </v-card-subtitle>
          
          <div class="itens_receita">
            <v-card-subtitle class="subtitle"> Ingredientes:
                <v-textarea class="input_add_receita" rows="5" label="Ingredientes" required v-model="ingredientes" />
            </v-card-subtitle>
            
            <v-card-subtitle class="subtitle"> Modo de preparo:
                <v-textarea class="input_add_receita" rows="5" label="Modo de preparo" required v-model="preparo" />
            </v-card-subtitle>
          </div>

          <div class="itens_receita">         
            <v-card-subtitle class="subtitle"> Mestre cuca:
                <v-textarea class="input_add_receita" rows="1" label="Autor(a)" required v-model="autor" />
            </v-card-subtitle>
            
            <input class="input_add_receita" style="magin-top: 10px;" type="file" @change="processFile($event)">
          </div>

        </v-container>
      </v-card-text>
      <div class="div_botao">
        <v-btn class="botao" text @click="close()">Cancelar</v-btn>
        <v-btn class="botao" text @click="add_receita()" :loading="loading" :disabled="loading">Cadastrar</v-btn>
      </div>
    </v-card>
  </v-dialog>
</template>

<script>

import AppApi from '~apijs'

export default {
    data () {
        return {
            receita: '',
            introducao: '',
            ingredientes: '',
            preparo: '',
            autor: '',
            foto: '',
            visible: false
        }
    },

    methods: {
        open() {
            this.visible=true;
        },
        close() {
            this.visible=false;
        },
        processFile(event){
            this.foto = event.target.files[0]
        },
        add_receita() {            
            const prato = AppApi.add_receita(this.receita, this.introducao, this.ingredientes, this.preparo, this.autor, this.foto).then(()=>{
                document.location.reload()
            })
            if (prato) {
                this.close()
            }
        }       
    }
}
</script>
<style>
 .title {
     display: flex;
     justify-content: center;
     align-items: center;
     color: #bb4b00;
     padding-top: 50px;
 }
 .subtitle {
     display: flex;
     flex-direction: column;
     align-items: baseline;
     width: 98%;
     margin: 10px;
     color: #bb4b00;
     font-weight: bold;
 }
 .input_add_receita {
     width: 100%;
 }
 .itens_receita {
     display: flex;
     width: 100%;
     align-items: center;
 }
 .div_botao {
     display: flex;
     justify-content: center;
     padding: 10px 20px;
 }
 .botao {
     margin: 10px 30px;
     color: #bb4b00 !important;
     font-weight: bold;
     border-radius: 20px;
 }
</style>