import './App.css';
import { useState, useEffect } from 'react';
import { Alert, Modal, ModalBody, ModalHeader } from 'react-bootstrap';
import { Link } from 'react-router-dom'

function App() {

  const [showModal, isShowModal] = useState(false);
  const [workflowName, setWorkflowName] = useState("");
  const [workflowFor, setWorkflowFor] = useState("");
  const [workflowDesc, setWorkflowDesc] = useState("");
  const [totalWorkflows, setTotalWorkflows] = useState([]);

  useEffect(() => {
    getWorkflows();
  }, []);

  async function getWorkflows() {
    let url = "http://localhost:8000/api/saveWorkflowDetails";
    const requestOptions = {
      method: 'GET',
    }
    await fetch(url, requestOptions).then((response) => response.json()).then((data) => {
      if (data.status === "success") {
        setTotalWorkflows(data.data)
      }
    })
  }

  function reset() {
    setWorkflowName("");
    setWorkflowFor("");
    setWorkflowDesc("");
  }

  async function saveWorkflowDetails() {
    let object = {
      workflowName: workflowName,
      workflowFor: workflowFor,
      workflowDesc: workflowDesc
    }

    const url = "http://localhost:8000/api/saveWorkflowDetails/";
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(object),
    }
    await fetch(url, requestOptions).then((response) => response.json()).then((data) => {
      switch (data.status) {
        case "success": {
          alert(data.message);
          getWorkflows();
          break;
        }
        case "error": {
          alert(data.message);
          getWorkflows();
          break;
        }
      }
    })
  }

  return (
    <div className="App">
      <header className="App-header">
        <h2>Workflows</h2>
        <button className='btn btn-primary' type='button' onClick={() => isShowModal(true)}>Create</button>
        <div className='container'>
          {totalWorkflows.map((obj) => (
            <div class="card" style={{ width: "18rem" }}>
              <div class="card-body">
                <h5 class="card-title">{obj.workflowName}</h5>
                <p class="card-text">{obj.workflowDesc}</p>
                <Link
                  to={{
                    pathname: '/create',
                  }}
                >
                  <button class="btn btn-primary">Create</button>
                </Link>
              </div>
            </div>
          ))}
        </div>
      </header>
      <Modal size='xl' show={showModal} onHide={() => isShowModal(false)}>
        <ModalHeader style={{ backgroundColor: "#282c34" }}>
          <h5 style={{ color: '#fff' }}>Create a workflow</h5>
        </ModalHeader>
        <ModalBody>
          <div className='container'>
            <div className='row' style={{ lineHeight: '1.5' }}>
              <div className='col-3'>
                <div className='form-group'>
                  <label className='form-label' htmlFor='workflow-name'>Workflow Name</label>
                  <input id='workflow-name' className='form-control' type='text' value={workflowName} onChange={(e) => setWorkflowName(e.target.value)}></input>
                </div>
              </div>
              <div className='col-3'>
                <div className='form-group'>
                  <label className='form-label' htmlFor='workflow-for'>Workflow For</label>
                  <input id='workflow-for' className='form-control' type='text' value={workflowFor} onChange={(e) => setWorkflowFor(e.target.value)}></input>
                </div>
              </div>
            </div>
            <div className='row' style={{ lineHeight: '1.5', marginTop: '30px', marginBottom: '30px' }}>
              <div className='col-3'>
                <div className='form-group'>
                  <label className='form-label' htmlFor='workflow-desc'>Description</label>
                  <input id='workflow-desc' className='form-control' type='text' value={workflowDesc} onChange={(e) => setWorkflowDesc(e.target.value)}></input>
                </div>
              </div>
            </div>
            <div className='btn-group'>
              <button className='btn btn-primary me-3' type='button' onClick={() => saveWorkflowDetails()}>Next</button>
              <button className='btn btn-dark' type='button' onClick={() => reset()}>Reset</button>
            </div>
          </div>
        </ModalBody>

      </Modal>
    </div>
  );
}

export default App;
