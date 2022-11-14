odoo.define('kanban_draggable.kanban_column',function(require){
"use strict";


var KanbanColumn = require('web.KanbanColumn');

KanbanColumn.include({
    start: function () {
        this._super.apply(this, arguments);

        if (this.record_options.sortable==false){
            this.$el.sortable( "disable" );
        }

    },

});
});