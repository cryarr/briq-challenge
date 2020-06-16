import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')


//this is where i need to be doing the analysis but i cannot figure out how to get this 
//to work
new Vue({
	el: '#app',
	vuetify,
	data: () => ({
		rating: 3,
	
	}),
	methods: {
		//this isnt working...
		getAnalysis: function(event){
			console.log(event)
		},
	}
})




//template function for textual analysis. but this is in TS. Will i have to go with angular?
//
// import * as tf from tensorflow
// const model = tf.sequential();
// model.compile({loss: 'meanSquaredError', optimizer: 'sgd'})
// use.load().then({
// 		const quotes = [getRandomQuotes()];
// 		model.embed(sentences).then(embeddings => {
//			embeddings.print(true /*)
// 		});
// });
