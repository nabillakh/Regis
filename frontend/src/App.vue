<template>
  <div>
    <h1>Tasks</h1>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        {{ task.fields.title }} - {{ task.fields.description }}
        <button @click="deleteTask(task.id)">Delete</button>
      </li>
    </ul>

    <h2>Create a new task</h2>
    <input v-model="newTaskTitle" placeholder="Title" />
    <input v-model="newTaskDescription" placeholder="Description" />
    <button @click="createTask">Create Task</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tasks: [],
      newTaskTitle: '',
      newTaskDescription: ''
    };
  },
  mounted() {
    this.fetchTasks();
  },
  methods: {
    fetchTasks() {
      axios.get('http://127.0.0.1:8000/api/tasks/')
        .then(response => {
          this.tasks = JSON.parse(response.data);
        })
        .catch(error => {
          console.error('Error fetching tasks:', error);
        });
    },
    createTask() {
      axios.post('http://127.0.0.1:8000/api/tasks/create/', {
        title: this.newTaskTitle,
        description: this.newTaskDescription
      })
      .then(() => {
        this.fetchTasks();  // Refresh the list of tasks
      })
      .catch(error => {
        console.error('Error creating task:', error);
      });
    },
    deleteTask(taskId) {
      axios.delete(`http://127.0.0.1:8000/api/tasks/delete/${taskId}/`)
        .then(() => {
          this.fetchTasks();  // Refresh the list of tasks
        })
        .catch(error => {
          console.error('Error deleting task:', error);
        });
    }
  }
};
</script>
