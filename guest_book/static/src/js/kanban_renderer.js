odoo.define('kanban_draggable.kanban_renderer',function(require){
"use strict";


var KanbanRenderer = require('web.KanbanRenderer');

KanbanRenderer.include({

    _setState: function (state) {
        this._super.apply(this, arguments);

        var arch = this.arch;
        var drag_drop = true;
        if (arch.attrs.disable_drag_drop_record) {
            if (arch.attrs.disable_drag_drop_record=='true') {
                this.columnOptions.draggable = false;
            }
        }

        this.recordOptions.sortable = true;
        if (arch.attrs.disable_sort_record) {
            if (arch.attrs.disable_sort_record=='true') {
                this.recordOptions.sortable = false;
            }
        }

        this.columnOptions.sortable = true;
        if (arch.attrs.disable_sort_column) {
            if (arch.attrs.disable_sort_column=='true') {
                this.columnOptions.sortable = false;
            }
        }
    },

    _renderGrouped: function (fragment) {
        this._super.apply(this, arguments);

        if (this.columnOptions.sortable==false){
            this.$el.sortable( "disable" );
        }

    },



});

});