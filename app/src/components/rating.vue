<template>
  <v-app id="inspire">
	<div id="rating">
		<v-rating v-model="rating" @input=getAnalysis($event)></v-rating>
	</div>
  </v-app>
</template>

<script>
  export default {
	name: 'rate',
	methods: {
		//it looks like this is the only way to actually get the number. but how?
		getAnalysis: function(event) {
			console.log(event);	
		}	
	}
  }
</script>
