var BetterTouchTool = Application('BetterTouchTool');
var updateDefinition = {
    "text": "newButtonText",
    "BTTStreamDeckBackgroundColor" : "255,85,100,255"
};
BetterTouchTool.update_stream_deck_widget("3FA8DF35-7605-4102-8BE6-70187F37EB3A",
    {json: JSON.stringify(updateDefinition)});
