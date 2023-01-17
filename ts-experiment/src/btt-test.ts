import "@jxa/global-type";
import { run } from "@jxa/run";

const updateBtt = () => {
	return run(() => {
		const btt = Application("BetterTouchTool");
		const update = {
			'BTTStreamDeckBackgroundColor': '0,85,100,255',
			text: "My Test"
		};
		btt.update_stream_deck_widget(
			'6564872B-4A13-4EE4-9199-3CDC369F84D6',
			{json: JSON.stringify(update)}
		);
		btt.set_persistent_string_variable("myTestVariable", {to:'some value', shared_secret:'mySecret'});
	});
};

updateBtt().then(output => {
	console.log(output);
}).catch(error => {
	console.log(error);
});
