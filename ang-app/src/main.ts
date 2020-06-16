import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
//dont know if this is the correct thing to do. I am unsure how ts relates to js
import * as use from '@tensorflow-models/universal-sentence-encoder';
import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

if (environment.production) {
  enableProdMode();
}


//getQuotes()
//xmlhttp request
// put into json
// quotelist =json['en']
// return quotelist

use.load().then(model => {
	const quotes = [
		getQuotes() //function for api call analysis
		];
	model.embed(quotes).then(embedddings => {
		embeddings.print(true /* verbose) //no idea what this is doing
	});
});

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
