<template>
  <div class="app-container">
    <el-alert
      title="最后一次操作日志"
      type="warning"
      :closable="false"
    ></el-alert>
    <virtual-list
      style="height: 360px; overflow-y: auto"
      :data-key="'id'"
      :data-sources="items"
      :data-component="itemComponent"
    />
  </div>
</template>

<script>
import virtualList from "vue-virtual-scroll-list";
import Item from "./log_item";
export default {
  components: { "virtual-list": virtualList },
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      itemComponent: Item,
      items: [],
    };
  },
  methods: {
    dataSource() {
      for (let i = 1; i <= 1000; i++) {
        this.items.push({
          id: i,
          name: i + "模拟字段 =====================",
        });
      }
    },
  },
  created() {
    this.dataSource();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>