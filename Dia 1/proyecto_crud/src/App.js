import React, { useState } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button'
import DeleteIcon from '@mui/icons-material/Delete';
import AddBoxIcon from '@mui/icons-material/AddBox';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import TextField from '@mui/material/TextField';
import FormControl from '@mui/material/FormControl';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';

import './App.css';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

export function App(id) {
  const curses = [
    { id: 1, nombre: 'Joshua', apellido: 'Arnao', nacionalidad: 'PERU' },
    { id: 2, nombre: 'Omaira', apellido: 'Palacios', nacionalidad: 'PERU' }
  ];

  const [name, setName] = useState('');

  const [curse, setCurse] = useState(curses);

  fetch (`https://http://127.1.0.0.1:8080/clientes${id}`, {
    method: 'GET'
  })
    .then((resp) => resp.jason())
    .then(function (curse) {
      
    })

  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);



  return (
    <div className="App">
      <div>
        <Stack direction="row" justifyContent="flex-end" alignItems="center" spacing={2}>
          <Button variant="outlined" color="success" startIcon={<AddBoxIcon />} onClick={handleOpen}>Agregar</Button>
          <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
          >
            <Box sx={style} componente="form">
              <Typography id="modal-modal-title" variant="h6" component="h2">
                Agregar nuevo usuario
              </Typography>
              <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
              </Typography>
              <FormControl fullWidth sx={{ m: 1, '& .MuiTextField-root': { m: 1, width: '48ch' }, }} >
                <TextField id="outlined-name" label="Nombre" variant="outlined" type="text"/>
                <TextField id="outlined-lastName" label="Apellido" variant="outlined" />
                <TextField id="outlined-country" label="Nacionalidad" variant="outlined" />
                <Button variant="contained" color="success">Agregar</Button>{''}
              </FormControl>
              
            </Box>
          </Modal>  
        </Stack>
        <TableContainer component={Paper}>
        <Table striped bordered hover>
          <TableHead>
            <TableRow>
              <TableCell align="center">ID</TableCell>
              <TableCell align="center">Nombre</TableCell>
              <TableCell align="center">Apellido</TableCell>
              <TableCell align="center">Nacionalidad</TableCell>
              <TableCell align="center" colSpan={2}>Editar</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {curse.map(resp =>
              <TableRow >
                <TableCell align="center">{resp.id}</TableCell>
                <TableCell align="center">{resp.nombre}</TableCell>
                <TableCell align="center">{resp.apellido}</TableCell>
                <TableCell align="center">{resp.nacionalidad}</TableCell>
                <TableCell>
                  <Stack direction="row" spacing={2} align="center" justifyContent="center">
                    <Button variant="contained" color="success">Editar</Button>{''}
                    <Button variant="outlined" color="error" startIcon={<DeleteIcon />}>Eliminar</Button>
                  </Stack>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
      </div>
      
    </div>
  );
}

export default App;
