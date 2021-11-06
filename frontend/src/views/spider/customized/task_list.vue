<template>
  <div class="mixin-components-container">
    <el-row :gutter="20" style="margin-top: 6px">
      <el-col :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>美团评论</span>
          </div>
          <div style="height: 150px">
            <el-form :model="meituanForm" :rules="meituanRules">
              <el-form-item prop="jId" label="景点ID">
                <el-input
                  style="width: 200px"
                  v-model="meituanForm.jId"
                  icon="el-icon-search"
                  placeholder="景点ID"
                >
                  景点ID
                </el-input>
              </el-form-item>

              <el-form-item prop="status" label="选项1">
                <el-select
                  v-model="xhsForm.status"
                  class="filter-item"
                  placeholder="Please select"
                >
                  <el-option
                    v-for="item in statusOptions"
                    :key="item"
                    :label="item"
                    :value="item"
                  />
                </el-select>
              </el-form-item>
            </el-form>

            <div slot="footer" class="dialog-footer">
              <el-button type="success" @click="handleMeituanUpdate()">
                <svg-icon icon-class="bug" /> 运行
              </el-button>

              <el-tooltip
                effect="dark"
                content="查看日志"
                placement="top-start"
              >
                <el-button
                  type="primary"
                  icon="el-icon-search"
                  @click="handleLog()"
                  >日志</el-button
                >
              </el-tooltip>
            </div>
          </div>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <!-- <mallki class-name="mallki-text" text="小红书任务 demo" /> -->
            <span>小红书任务 demo</span>
          </div>
          <div style="height: 150px">
            <el-form :model="xhsForm" :rules="xhsRules">
              <el-form-item prop="title" label="关键词">
                <el-input
                  style="width: 200px"
                  v-model="xhsForm.title"
                  icon="el-icon-search"
                  placeholder="搜索关键词"
                >
                  标题
                </el-input>
              </el-form-item>

              <el-form-item prop="status" label="选项1">
                <el-select
                  v-model="xhsForm.status"
                  class="filter-item"
                  placeholder="Please select"
                >
                  <el-option
                    v-for="item in statusOptions"
                    :key="item"
                    :label="item"
                    :value="item"
                  />
                </el-select>
              </el-form-item>
            </el-form>

            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false"> 重置 </el-button>

              <el-button type="success" @click="updateData()">
                <svg-icon icon-class="bug" /> 运行
              </el-button>
            </div>
          </div>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>马蜂窝任务 demo</span>
          </div>
          <div style="height: 150px">
            <el-form :model="mafengwoForm" :rules="mafengwoRules">
              <el-form-item prop="jId" label="景点ID">
                <el-input
                  style="width: 200px"
                  v-model="mafengwoForm.jId"
                  icon="el-icon-search"
                  placeholder="景点ID"
                >
                  标题
                </el-input>
              </el-form-item>

              <el-form-item prop="status" label="选项1">
                <el-select
                  v-model="mafengwoForm.status"
                  class="filter-item"
                  placeholder="Please select"
                >
                  <el-option
                    v-for="item in statusOptions"
                    :key="item"
                    :label="item"
                    :value="item"
                  />
                </el-select>
              </el-form-item>
            </el-form>

            <div slot="footer" class="dialog-footer">
              <el-button
                v-if="this.taskStatus == 1"
                type="success"
                @click="onSubmit()"
              >
                <svg-icon icon-class="bug" /> 运行</el-button
              >
              <el-button v-else type="success"
                ><i size="mini" class="el-icon-loading"></i> 运行中</el-button
              >

              <el-tooltip
                effect="dark"
                content="查看日志"
                placement="top-start"
              >
                <el-button type="primary" icon="el-icon-search"
                  >任务日志</el-button
                >
              </el-tooltip>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PanThumb from "@/components/PanThumb";
import MdInput from "@/components/MDinput";
import Mallki from "@/components/TextHoverEffect/Mallki";
import DropdownMenu from "@/components/Share/DropdownMenu";
import waves from "@/directive/waves/index.js"; // 水波纹指令
import { start_task } from "@/api/spider";

export default {
  name: "ComponentMixinDemo",
  components: {
    PanThumb,
    MdInput,
    Mallki,
    DropdownMenu,
  },
  directives: {
    waves,
  },
  data() {
    const validate = (rule, value, callback) => {
      // if (value.length !== 6) {
      //   callback(new Error("请输入六个字符"));
      // } else {
      //   callback();
      // }
    };
    return {
      temp: {
        status: "",
      },
      taskStatus: 0,

      statusOptions: ["1", "2"],
      meituanForm: {
        jId: null,
        status: "",
      },
      xhsForm: {
        title: "",
        status: "",
      },
      mafengwoForm: {
        jId: "",
        status: "",
      },
      xhsRules: {
        title: [{ required: true, trigger: "change", validator: validate }],
        status: [{ required: true, trigger: "change", validator: validate }],
      },
      mafengwoRules: {
        jId: [{ required: true, trigger: "change", validator: validate }],
        status: [{ required: true, trigger: "change", validator: validate }],
      },
      meituanRules: {
        jId: [{ required: true, trigger: "change", validator: validate }],
        status: [{ required: true, trigger: "change", validator: validate }],
      },

      articleList: [
        {
          title: "基础篇",
          href: "https://juejin.im/post/59097cd7a22b9d0065fb61d2",
        },
        {
          title: "登录权限篇",
          href: "https://juejin.im/post/591aa14f570c35006961acac",
        },
        {
          title: "实战篇",
          href: "https://juejin.im/post/593121aa0ce4630057f70d35",
        },
        {
          title: "vue-admin-template 篇",
          href: "https://juejin.im/post/595b4d776fb9a06bbe7dba56",
        },
        {
          title: "v4.0 篇",
          href: "https://juejin.im/post/5c92ff94f265da6128275a85",
        },
        {
          title: "优雅的使用 icon",
          href: "https://juejin.im/post/59bb864b5188257e7a427c09",
        },
      ],
    };
  },
  created() {},
  methods: {
    deleteTask(taskId) {
      const self = this;
      var data = {
        taskId,
      };
      // 二次确认删除
      self
        .$confirm("确定要删除吗？", "提示", {
          type: "warning",
        })
        .then(() => {
          delete_task(data).then((res) => {
            if (res.code === 20000) {
              self.$message.success("删除成功");
              self.reload();
            }
          });
        })
        .catch(() => {});
    },

    handleMeituanUpdate() {
      this.$message.success("抓取中");

      // start_task(this.meituanForm).then((res) => {
      // if (res.code === 20000) {
      this.$notify({
        title: "成功",
        message:
          // res.data.taskName +
          " 更新成功 " + new Date().toLocaleTimeString(),
        type: "success",
        duration: 0,
      });
      // } else {
      //   this.$message.error(res.data);
      // }
      // });
    },

    handleLog() {
      const self = this;
      var taskId = 12346;
      self.$router.push(`/task_log/${taskId}`);
    },

    // 睡一觉
    // sleep(delay) {
    //   var start = new Date().getTime();
    //   while (new Date().getTime() - start < delay) {
    //     continue;
    //   }
    // },
  },
};
</script>

<style scoped>
.mixin-components-container {
  background-color: #f0f2f5;
  padding: 30px;
  min-height: calc(100vh - 84px);
}
.component-item {
  min-height: 100px;
}
</style>
