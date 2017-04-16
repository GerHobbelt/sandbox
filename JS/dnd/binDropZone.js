"use strict";

/**
 * Drop zone that destroys shapes dropped into its pockets.
 * @extends DropZone
 * @constructor
 */

function BinDropZone(options) {
  DropZone.apply(this, arguments);
}

extend(BinDropZone, DropZone);

BinDropZone.prototype.onDragEnd = function(dragObject, pocket) {
  dragObject.remove();
};