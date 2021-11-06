<template>
  <div class="app-container">
    <el-row :gutter="20">
      <!-- 任务 -->
      <el-col
        :xs="24"
        :sm="24"
        :md="12"
        :lg="16"
        :xl="12"
        style="margin-bottom: 10px"
      >
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>任务</span>
          </div>

          <el-table
            :key="tableKey"
            :data="taskList"
            aria-setsize
            fit
            highlight-current-row
            style="width: 100%"
          >
            <el-table-column align="center" label="任务名称" min-width="130px">
              <template slot-scope="{ row }">
                <el-button type="success" size="mini" plain>{{ row.function_name }}</el-button>
              </template>
            </el-table-column>


            <el-table-column min-width="110px" align="center" label="最后执行状态">
              <template slot-scope="{ row }">
                <el-button type="success" icon="el-icon-check" circle></el-button>

              </template>
            </el-table-column>

            <el-table-column label="操作" align="center" min-width="250">
              <template slot-scope="{ row, $index }">
                <div>
                  <el-button type="primary" size="mini"
                  >执行任务
                  </el-button
                  >
                  <el-button type="primary" size="mini"
                  >参数设置
                  </el-button
                  >
                  <el-button type="" size="mini"
                  >查看结果
                  </el-button
                  >
                </div>
              </template>
            </el-table-column>
          </el-table>

          <pagination
            v-show="taskTotal > 0"
            :total="taskTotal"
            :page.sync="listQuery.page"
            :limit.sync="listQuery.limit"
            @pagination="getList"
          />
        </el-card>
      </el-col>

      <!-- 定时任务 -->
      <el-col :xs="24" :sm="24" :md="12" :lg="16" :xl="12">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>定时任务</span>
          </div>

          <el-table
            :key="tableKey"
            :data="cronList"
            aria-setsize
            fit
            highlight-current-row
            style="width: 100%"
          >
            <el-table-column align="center" label="任务名称" min-width="120px">
              <template slot-scope="{ row }">
                <el-button type="success" size="mini" plain>{{ row.function_name}}</el-button>
              </template>
            </el-table-column>

            <el-table-column min-width="340px" align="center" label="定时表达式">
              <template slot-scope="{ row }">
                <el-button type="danger" size="mini" plain>月 {{ row.month }}、 周 {{ row.weekday }}、 天 {{ row.day }}、 时 {{ row.hour }}、 分 {{ row.minute }}、 秒 {{ row.second }} </el-button>
              </template>
            </el-table-column>

            <el-table-column min-width="120px" align="center" label="下次执行">
              <template slot-scope="{ row }">
                <el-button type="" size="mini" plain
                >{{ row.next_run || "待定" }}
                </el-button>
              </template>
            </el-table-column>

            <el-table-column label="操作" align="center" min-width="220">
              <template slot-scope="{ row, $index }">
                <div>
                  <el-button type="" size="mini" @click="handleNodeDelete(row)"
                  >任务详情
                  </el-button
                  >
                  <el-button type="" size="mini" @click="handleNodeDelete(row)"
                  >查看结果
                  </el-button
                  >
                </div>
              </template>
            </el-table-column>
          </el-table>

          <pagination
            v-show="cronTotal > 0"
            :total="cronTotal"
            :page.sync="listQuery.page"
            :limit.sync="listQuery.limit"
            @pagination="getList"
          />
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import {get_task_list} from "@/api/arq";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
  name: "Task",
  components: {Pagination},
  directives: {waves},
  data() {
    return {
      tableKey: 0,
      cronTotal: 0,
      taskTotal: 0,
      cronList:[],
      taskList:[],
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
      },
    };
  },
  created() {
    this.getList();
  },
  methods: {
    getList() {
      get_task_list().then((response) => {
        this.cronList = response.results.cron_list;
        this.taskList = response.results.task_list;
        this.cronTotal = response.results.cron_num || 2;
        this.taskTotal = response.results.task_num || 2;
        setTimeout(() => {
        }, 1.5 * 1000);
      });
    },

    // handleRun(row) {
    //   console.log("listQuery: ", this.listQuery);
    //   const data = {
    //     task: "add",
    //     args: [5555, 4444],
    //     kwargs: {},
    //     job_id: "",
    //     job_retry: 1,
    //   };
    //   this.$confirm("确认运行该任务?", "警告", {
    //     confirmButtonText: "确定",
    //     cancelButtonText: "取消",
    //     type: "warning",
    //   }).then(() =>
    //     run_tasks(data).then((response) => {
    //       this.$notify({
    //         title: "Success",
    //         message: "成功派发一个任务",
    //         type: "success",
    //         duration: 2000,
    //       });
    //       console.log("response: ", response);
    //       setTimeout(() => {}, 3 * 1000);
    //     })
    //   );
    // },

    // 删除节点
    handleNodeDelete(row, index) {
      this.$notify({
        title: "删除节点",
        message: "请联系管理员删除",
        type: "error",
        duration: 2000,
      });
    },
  },
};
</script>
