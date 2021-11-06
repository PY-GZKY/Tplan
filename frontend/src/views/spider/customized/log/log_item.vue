<template>
    <!-- 显示的数据源 -->
    <div>{{ index }} - {{ source.name }}</div>
</template>

<script>
    export default {
        name: "item-component",
        props: {
            index: {
                // index of current item
                type: Number,
            },
            source: {
                // here is: {id: '1', name: 'abc'}
                type: Object,
                default() {
                    return {};
                },
            },
        },
    };
</script>